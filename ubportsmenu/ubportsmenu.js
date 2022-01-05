var ubportsmenu = {
  menuBaseUrl: "https://odoomenu.codefounders.nl//wp-content/plugins/odoomenu/",

  execRequest(fileToGet, executeThis) {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", this.menuBaseUrl + fileToGet, true); // false will basically be ignored
    xhr.onreadystatechange = () => {
      if (xhr.readyState == XMLHttpRequest.DONE) {
        if (xhr.status == 200) {
          executeThis(xhr);
        } /*if (xhr.status == 404)*/ else {
          console.log("Cannot load ubports menu.");
        }
      }
    };
    xhr.send();
  },

  insertMenuAsHtml(respone) {
    let divEl = document.createElement("div");
    let classAttr = document.createAttribute("class");
    classAttr.value = "ubpm";
    divEl.setAttributeNode(classAttr);
    divEl.style.display = "none";
    divEl.innerHTML = respone.responseText;
    document.body.insertBefore(divEl, document.body.firstElementChild);
  },

  addScriptToHead(filename) {
    let scriptEl = document.createElement("script");
    scriptEl.src = this.menuBaseUrl + filename;
    scriptEl.defer = true;
    document.head.appendChild(scriptEl);
  },

  addStylesheetToHead(filename) {
    let linkEl = document.createElement("link");
    linkEl.rel = "stylesheet";
    linkEl.href = this.menuBaseUrl + filename;
    document.head.appendChild(linkEl);
  },

  execAfterFullpageLoad() {
    window.onload = (ev) => {
      document.querySelector(".ubpm").style.display = "block";
    };
  },

  /** OLD */
  execAfterFullpageLoadv1() {
    document.onreadystatechange = function () {
      if (document.readyState == "complete") {
        document.querySelector(".ubpm").style.visibility = "visible";
      }
    };
  },

  /** The menu is sometimes not shown, this occurs when the page load event is triggered before the menu is loaded.
   * This delayed enabling of the visibility fixes this.
   */
  async waitsometime() {
    await new Promise((r) => setTimeout(r, 2000));
    console.log("XXX - Fully loaded");
    document.querySelector(".ubpm").style.visibility = "visible";
  },

  buildMenu() {
    this.execAfterFullpageLoad();
    this.execRequest("odoomenu-minimal.html", this.insertMenuAsHtml);
    this.addStylesheetToHead("web.assets_frontend.css");
    this.addScriptToHead("web.assets_common_lazy.js");
  },
};

ubportsmenu.buildMenu();
