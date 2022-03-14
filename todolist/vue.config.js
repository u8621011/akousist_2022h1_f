module.exports = {
  transpileDependencies: [
    'vuetify'
    ],
    devServer: {
        proxy: 'http://localhost:5000', // solve cors the proxy server, ref: https://stackoverflow.com/questions/55883984/vue-axios-cors-policy-no-access-control-allow-origin
    }
}
