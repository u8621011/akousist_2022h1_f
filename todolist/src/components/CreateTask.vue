<template>
    <v-container>
        <v-row justify="center" class="ma-5">
            <v-col xs="12" sm="8">
                <v-card>
                    <v-toolbar color="blue darken-4" dark>
                        <v-toolbar-title class="headline">Create Todo Task</v-toolbar-title>
                    </v-toolbar>

                    <v-list two-line subheader>
                        <v-subheader class="headline">{{stepHintText}}</v-subheader>
                        <v-list-item>
                            <v-list-item-content>
                                <v-list-item-title>
                                    <v-text-field v-model="taskTitle" id="taskTitle" name="taskTitle" label="Task Title"
                                                  :disabled="taskObject && taskObject.title && taskObject.title.length > 0"
                                                  @keyup.enter="addTodo" />
                                </v-list-item-title>
                            </v-list-item-content>
                        </v-list-item>

                        <v-list-item v-if="showDescField">
                            <v-text-field v-model="taskDesc" id="todoDesc" name="desc" label="Task Desc"
                                          :disabled="taskObject && taskObject.desc && taskObject.desc.length > 0"
                                          @keyup.enter="updateTaskDesc" />
                        </v-list-item>

                        <v-list-item>
                            <v-list-item-content>
                                <v-list-item-title>
                                    <v-btn v-if="isCreating" v-on:click="onBtnClicked()">
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
            taskObject: null,
            todos: [],
        }),
        methods: {
            onBtnClicked: function () {
                if (this.taskObject) {
                    this.updateTask();
                } else {
                    this.createTask();
                }
            },
            createTask: async function () {
                const value = this.taskTitle && this.taskTitle.trim();
                if (!value) {
                    return;
                }
                try {
                    let res = await this.axios.post("api/tasks", {
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
            updateTask: async function () {
                const value = this.taskDesc && this.taskDesc.trim();
                if (!value) {
                    return;
                }
                try {
                    let res = await this.axios.put("/api/tasks/" + this.taskId, {
                        desc: this.taskDesc,
                    });
                    console.log('res: ' + JSON.stringify(res));
                    let data = res.data;
                    if (data.success) {
                        this.taskObject.desc = this.taskDesc;
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
            isCreating: function () {
                if (!this.taskObject || !this.taskObject.desc) {
                    return true;
                }
                return false;
            },
            stepHintText: function () {
                if (!this.taskObject) {
                    return 'Step1. Input the task title and click create to start';
                }

                if (!this.taskObject.desc) {
                    return 'Step2. Input task desc and click update desc to finish.';
                }
                return 'Task Detail';
            },
            showDescField: function () {
                return this.taskObject;
            },
            btnText: function () {
                if (!this.taskObject) {
                    return 'Create Task';
                }
                if (!this.taskObject.desc) {
                    return 'Update Desc';
                }
                return null;
            },
        }
    }
</script>
