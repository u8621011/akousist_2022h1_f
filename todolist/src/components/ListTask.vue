<template>
    <v-container>
        <v-row justify="center" class="ma-5">
            <v-col xs="12" sm="8">
                <v-card>
                    <v-toolbar color="blue darken-4" dark>
                        <v-toolbar-side-icon></v-toolbar-side-icon>
                        <v-toolbar-title class="headline">List Tasks</v-toolbar-title>
                    </v-toolbar>

                    <v-list subheader two-line flat>
                        <v-subheader class="subheading" v-if="tasks.length == 0">You have 0 Tasks, add some</v-subheader>
                        <v-subheader class="subheading" v-else>Your Tasks</v-subheader>

                        <v-list-item-group>
                            <v-list-item v-for="(t, i) in tasks" :key=t.id>
                                <template #default="{ active}">
                                    <v-list-item-content>
                                        <v-list-item-title :class="{ done: active }">{{ t.title }}</v-list-item-title>
                                        <v-list-item-subtitle>{{fmtItemState(t)}}</v-list-item-subtitle>
                                    </v-list-item-content>
                                    <v-btn fab ripple small color="green" class="mr-3" @click="openTask(t)">
                                        <v-icon class="white--text">mdi-eye</v-icon>
                                    </v-btn>
                                    <v-btn fab ripple small color="red" @click="removeTask(t, i)">
                                        <v-icon class="white--text">mdi-close</v-icon>
                                    </v-btn>
                                </template>
                            </v-list-item>
                        </v-list-item-group>
                    </v-list>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
    export default {
        name: 'ListTask',

        data: () => ({
            tasks: [
                {
                    id: 1,
                    active: false,
                    title: 'title 1'
                },
                {
                    id: 2,
                    active: false,
                    title: 'title 2'
                },
                {
                    id: 3,
                    active: false,
                    title: 'title 3'
                },

            ],
        }),

        methods: {
            fmtItemState: function (task) {
                let stateText = 'State: ';

                if (task.desc) {
                    return stateText  + 'Finished';
                }

                return stateText + 'Step2';
            },
            getTasks: async function () {
                try {
                    let res = await this.axios.get("/api/tasks");
                    let data = res.data;

                    if (data.success) {
                        this.tasks = data.data;
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
            removeTask: async function (task, taskIndex) {
                try {
                    let res = await this.axios.delete("/api/tasks/" + task.id);
                    let data = res.data;

                    if (data.success) {
                        this.tasks.splice(taskIndex, 1);
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
            openTask: async function (task) {
                this.$router.push('/tasks/' + task.id);
            }
        },
        mounted: async function () {
            await this.getTasks();
        },
    }
</script>
