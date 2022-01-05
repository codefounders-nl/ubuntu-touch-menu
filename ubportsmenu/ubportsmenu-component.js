var vm = Vue.component('ubports-menu', {
    data() {
        return {
            ubportsmenu: 'Loading menu...',
            menuBaseUrl: "https://odoomenu.codefounders.nl//wp-content/plugins/odoomenu/"
        }
    },
    methods: {
        setUbportsmenu(menu) {
            this.ubportsmenu = menu;
        },

        execRequest: function(fileToGet, executeThis) {
            var xhr = new XMLHttpRequest();
            xhr.open('GET', this.menuBaseUrl + fileToGet, true); // false will basically be ignored
            xhr.onreadystatechange = () => {
                if (xhr.readyState == XMLHttpRequest.DONE) {
                    if (xhr.status == 200) {
                        executeThis(xhr);
                    } else /*if (xhr.status == 404)*/ {
                        console.log("Cannot load ubports menu.");
                    }
                }
            }
            xhr.send();
        },
        insertMenuAsHtml(respone) {
            let divEl = document.createElement("div");
            divEl.innerHTML = respone.responseText;

            // var h = document.getElementById("graph_header");
            document.body.insertBefore(divEl, document.body.firstElementChild);

            // document.body.appendChild(divEl);

        },
        addScriptToHead(filename) {
            let scriptEl = document.createElement("script");
            scriptEl.src = this.menuBaseUrl + filename;
            document.head.appendChild(scriptEl);
        },
        addStylesheetToHead(filename) {
            let linkEl = document.createElement("link");
            linkEl.rel = "stylesheet";
            linkEl.href = this.menuBaseUrl + filename;
            document.head.appendChild(linkEl);
        }
    },
    mounted() {
        // this.$http.get('/https://odoomenu.codefounders.nl//wp-content/plugins/odoomenu//odoomenu-minimal.html').then(response => {
        //     this.ubportsmenu = response.data;
        this.addStylesheetToHead("web.assets_common.css");
        this.addStylesheetToHead("web.assets_frontend.css");
        this.addStylesheetToHead("odoomenu-plugin.css");
        this.addScriptToHead("web.assets_common_lazy.js");
        this.execRequest('odoomenu-minimal.html', this.insertMenuAsHtml);
        this.ubportsmenu="";
    },
    template: '<div>{{ ubportsmenu }}</div>'
})