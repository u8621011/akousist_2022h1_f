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
                        <v-subheader class="subheading" v-if="todos.length == 0">You have 0 Tasks, add some</v-subheader>
                        <v-subheader class="subheading" v-else>Your Tasks</v-subheader>

                        <v-list-item-group>
                            <v-list-item v-for="(todo, i) in todos" :key=todo.Id>
                                <template #default="{ active, toggle }">
                                    <v-list-item-action>

                                        <v-checkbox v-model="todo.active" @click="toggle"></v-checkbox>
                                    </v-list-item-action>

                                    <v-list-item-content>
                                        <v-list-item-title :class="{
                  done: active
                  }">{{ todo.title }}</v-list-item-title>
                                        <v-list-item-subtitle>Added on: {{ date }}{{ ord }} {{ day }} {{ year }}</v-list-item-subtitle>
                                    </v-list-item-content>
                                    <v-btn fab ripple small color="red" v-if="active" @click="removeTodo(i)">
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
            isCreating: true,
            newTodo: "",
            todos: [
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
    }
</script>
