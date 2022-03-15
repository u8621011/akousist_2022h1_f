<template>
    <v-container>
        <v-row justify="center" class="ma-5">
            <v-col xs="12" sm="8">
                <v-card>
                    <v-toolbar color="blue darken-4" dark>
                        <v-toolbar-title class="headline">{{panelTitle}}</v-toolbar-title>
                    </v-toolbar>

                    <v-list two-line subheader>
                        <v-subheader class="headline" v-if="inStep < 4">{{stepTitle}}</v-subheader>
                        <v-list-item v-if="inStep >= 1">
                            <v-list-item-content>
                                <p style="color:red">{{stepHintText}}</p>
                            </v-list-item-content>
                        </v-list-item>

                        <v-list-item v-if="inStep >= 1">
                            <v-list-item-content>
                                <v-list-item-title>
                                    <v-text-field v-model="taskTitle" id="taskTitle" name="taskTitle" label="Task Title"
                                                  :disabled="taskObject && taskObject.title && taskObject.title.length > 0"
                                                  @keyup.enter="onBtnClicked()" />
                                </v-list-item-title>
                            </v-list-item-content>
                        </v-list-item>

                        <v-list-item v-if="inStep == 2">
                            <v-file-input @change="previewImage" accept="image/jpeg, image/png, image/gif, image/bmp"
                                          v-model="pictureImage">
                            </v-file-input>
                        </v-list-item>
                        <v-list-item v-if="inStep >= 2 && pictureUrl">
                            <v-list-item-content>
                                <v-list-item-title>Task Image</v-list-item-title>
                                <v-img :src="pictureUrl"></v-img>
                            </v-list-item-content>
                        </v-list-item>

                        <v-list-item v-if="inStep >= 3">
                            <v-text-field v-model="taskDesc" id="tasjDesc" name="tasjDesc" label="Task Desc"
                                          :disabled="taskObject && taskObject.desc && taskObject.desc.length > 0"
                                          @keyup.enter="onBtnClicked()" />
                        </v-list-item>

                        <v-list-item v-if="inStep < 4">
                            <v-list-item-content>
                                <v-list-item-title>
                                    <v-btn v-on:click="onBtnClicked()">
                                        <span class="mx-auto">{{btnText}}</span>
                                    </v-btn>
                                </v-list-item-title>
                            </v-list-item-content>
                        </v-list-item>
                    </v-list>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>
<script>
    export default {
        name: 'CreateTask',
        props: {
            taskId: {
                type: String,
                default: null,
            },
        },
        data: () => ({
            // input field data
            taskTitle: "",
            taskDesc: null,
            pictureUrl: null,
            pictureImage: null,

            taskObject: null,
            todos: [],
        }),
        methods: {
            previewImage() {
                const fileType = this.pictureImage['type'];
                const validImageTypes = ['image/gif', 'image/jpeg', 'image/png', 'image/bmp'];
                if (validImageTypes.includes(fileType)) {
                    this.pictureUrl = URL.createObjectURL(this.pictureImage)
                } else {
                    alert('Invalid file type, please select gir/jpeg/png/bmp file');
                }
            },
            onBtnClicked: function () {
                if (this.taskObject) {
                    this.updateTask();
                } else {
                    this.createTask();
                }
            },
            createTask: async function () {
                const value = this.taskTitle && this.taskTitle.trim();
                if (this.inStep == 1 && !value) {
                    return;
                }

                try {
                    let res = await this.axios.post("/api/tasks", {
                        title: value,
                    });
                    console.log('res: ' + JSON.stringify(res));
                    let data = res.data;
                    if (data.success) {
                        this.taskObject = data.data;
                        let taskId = this.taskObject.id;
                        this.$router.push('/tasks/' + taskId);
                    } else {
                        alert(data.error);
                    }
                } catch (error) {
                    if (error.response) {
                        // 當狀態碼不在 validateStatus 設定的範圍時進入, 401 感覺會跑來這。待確認
                        // 有 data / status / headers 參數可用
                        console.log(error.response.status + error.response.error);
                    } else if (error.request) {
                        // 發送請求，但沒有接到回應
                        // error.request is an instance of XMLHttpRequest in the browser
                        // and an instance of http.ClientRequest in node.js
                        console.log(error.request);
                    } else {
                        // 在設定 request 時出錯會進入此
                        console.log("Error", error.error);
                    }
                }
            },
            getFormData: function () {
                const formData = new FormData();

                if (this.pictureImage) {
                    formData.append("file", this.pictureImage);
                }

                if (this.taskDesc) {
                    formData.append('desc', this.taskDesc);
                }

                return formData;
            },
            updateTask: async function () {
                // validation
                if (this.inStep == 2) {
                    if (!this.pictureImage) {
                        alert('Please select image file');
                        return;
                    }

                    // check is image file or not
                    const fileType = this.pictureImage['type'];
                    const validImageTypes = ['image/gif', 'image/jpeg', 'image/png', 'image/bmp'];
                    if (!validImageTypes.includes(fileType)) {
                        alert('Invalid file type, please select gir/jpeg/png/bmp file');
                        return;
                    }
                } else if (this.inStep == 3) {
                    const value = this.taskDesc && this.taskDesc.trim();
                    if (!value) {
                        alert('Please input desc');
                        return;
                    }
                }

                try {
                    let formData = this.getFormData();
                    let res = await this.axios.put("/api/tasks/" + this.taskId, formData);
                    console.log('res: ' + JSON.stringify(res));
                    let data = res.data;
                    if (data.success) {
                        let item = data.data;
                        if (this.inStep == 2) {
                            this.$set(this.taskObject, 'filename', item.filename);
                            this.$set(this.taskObject, 'origin_filename', item.origin_filename);
                        } else if (this.inStep == 3) {
                            this.$set(this.taskObject, 'desc', this.taskDesc);
                        }
                    } else {
                        alert(data.error);
                    }
                } catch (error) {
                    if (error.response) {
                        // 當狀態碼不在 validateStatus 設定的範圍時進入, 401 感覺會跑來這。待確認
                        // 有 data / status / headers 參數可用
                        console.log(error.response.status + error.response.error);
                    } else if (error.request) {
                        // 發送請求，但沒有接到回應
                        // error.request is an instance of XMLHttpRequest in the browser
                        // and an instance of http.ClientRequest in node.js
                        console.log(error.request);
                    } else {
                        // 在設定 request 時出錯會進入此
                        console.log("Error", error.error);
                    }
                }
            },
            initData: async function () {
                if (!this.taskId) {
                    return;
                }
                try {
                    let res = await this.axios.get("/api/tasks/" + this.taskId);
                    console.log('res: ' + JSON.stringify(res));
                    let data = res.data;
                    if (data.success) {
                        this.taskObject = data.data;

                        this.taskTitle = this.taskObject.title;
                        this.taskDesc = this.taskObject.desc;

                        if (this.taskObject.filename) {
                            this.pictureUrl = '/upload/' + this.taskObject.filename;
                        }
                    } else {
                        alert(data.error);
                    }
                } catch (error) {
                    if (error.response) {
                        // 當狀態碼不在 validateStatus 設定的範圍時進入, 401 感覺會跑來這。待確認
                        // 有 data / status / headers 參數可用
                        console.log(error.response.status + error.response.error);
                    } else if (error.request) {
                        // 發送請求，但沒有接到回應
                        // error.request is an instance of XMLHttpRequest in the browser
                        // and an instance of http.ClientRequest in node.js
                        console.log(error.request);
                    } else {
                        // 在設定 request 時出錯會進入此
                        console.log("Error", error.error);
                    }
                }
            },
        },
        mounted: async function () {
            await this.initData();
        },
        computed: {
            inStep: function () {
                if (!this.taskObject) {
                    return 1;
                }

                if (!this.taskObject.filename) {
                    return 2;
                }

                if (!this.taskObject.desc) {
                    return 3;
                }

                return 4;
            },
            panelTitle: function () {
                switch (this.inStep) {
                    case 1:
                    case 2:
                    case 3:
                        return 'Create Todo Task';
                    case 4:
                        return 'Task Detail';
                    default:
                        return 'Unknown state';
                }
                
            },
            stepTitle: function () {
                switch (this.inStep) {
                    case 1:
                        return 'Step1';
                    case 2:
                        return 'Step2';
                    case 3:
                        return 'Step3';
                    case 4:
                        return 'Finished';

                    default:
                        return 'Unknown Step';
                }
            },
            stepHintText: function () {
                switch (this.inStep) {
                    case 1:
                        return 'Input the task title and click create to start';
                    case 2:
                        return 'Select image file and click update desc to finish.';
                    case 3:
                        return 'Input task desc and click update desc to finish.';
                    default:
                        return 'Unknown hint';
                }
            },
            btnText: function () {
                if (!this.taskObject) {
                    return 'Create Task';
                }

                if (!this.taskObject.filename) {
                    return 'Upload Image';
                }

                if (!this.taskObject.desc) {
                    return 'Update Desc';
                }
                return null;
            },
        }
    }
</script>
