<template>
    <v-container>
        <v-row justify="center" class="ma-5">
            <v-col xs="12" sm="8">
                <v-card>
                    <v-toolbar color="blue darken-4" dark>
                        <v-toolbar-title class="headline">Create Todo Task</v-toolbar-title>
                    </v-toolbar>

                    <v-list two-line subheader>
                        <v-subheader class="headline">Input the task name and click create to start</v-subheader>
                        <v-list-item>
                            <v-list-item-content>
                                <v-list-item-title>
                                    <v-text-field v-model="newTodo" id="newTodo" name="newTodo" label="Type your task" @keyup.enter="addTodo" />
                                </v-list-item-title>
                            </v-list-item-content>
                        </v-list-item>

                    </v-list>

                    <v-btn v-if="isCreating" v-on:click="createTask()">
                        <span class="mx-auto">Create</span>
                    </v-btn>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
    export default {
        name: 'CreateTask',

        data: () => ({
            isCreating: true,
            newTodo: "",
            taskObject: null,
            todos: [],
        }),

        methods: {
            createTask: async function () {
                const value = this.newTodo && this.newTodo.trim();
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
                        alert('taskId: ' + taskId);
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
            addTodo() {
                const value = this.newTodo && this.newTodo.trim();
                if (!value) {
                    return;
                }

                this.todos.push({
                    title: this.newTodo,
                    done: false
                });
                this.newTodo = "";
            },

            removeTodo(index) {
                this.todos.splice(index, 1);
            },
        },

        computed: {
            isCreating: function () {
                if (!this.taskObject || !this.taskObject.desc) {
                    return true;
                }

                return false;
            },
            /*
            stepHintText: function () {

            },
            showDescField: function () {

            },
            btnText: function () {

            },*/
        }
    }
</script>
