<template>
    <v-container>
        <v-row justify="center" class="ma-5">
            <v-col xs="12" sm="8">
                <v-card>
                    <v-toolbar color="blue darken-4" dark>
                        <v-toolbar-side-icon></v-toolbar-side-icon>
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

                    <v-btn>
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
            todos: [],
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

        filters: {
            capitalize: function (value) {
                if (!value) return "";
                value = value.toString();
                return value.charAt(0).toUpperCase() + value.slice(1);
            }
        }
    }
</script>
