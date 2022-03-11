<template>
    <v-app>
        <v-app-bar app
                   color="primary"
                   dark>
            <h3>TODO App</h3>

            <v-spacer></v-spacer>

            <v-btn href="/"
                   text>
                <v-icon>mdi-archive-plus</v-icon>
            </v-btn>
            <v-btn href="/tasks"
                   text>
                <v-icon>mdi-format-list-bulleted-square</v-icon>
            </v-btn>
        </v-app-bar>
        <v-main>
            <router-view :user="user"></router-view>
        </v-main>
    </v-app>
</template>

<script>
    export default {
        name: 'App',

        components: {
        },

        data() {
            return {
            }
        },
        methods: {
            
        },

    };
</script>
