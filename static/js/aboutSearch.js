let aboutSearchBar = document.getElementById("about_search");
let list = document.getElementById("list");

aboutSearchBar.addEventListener("input", function() {
    let searchTerm = aboutSearchBar.value.toLowerCase();
    let listItems = list.getElementsByClassName("list_item");
    let noItemMsg = document.getElementById("NoItemMsg");
    let numOfItems = 0;
    document.getElementById("about_tsp_title").style.display = "none";
    document.getElementById("about_tsp_pic").style.display = "none";
    document.getElementById("about_box").style.display = "none";
    list.style.display = "block";

    for (let i = 0; i < listItems.length; i++) {
        let listItem = listItems[i];
        let itemText = listItem.textContent.toLowerCase();
        if (itemText.indexOf(searchTerm) !== -1) {
            listItem.style.display = "block";
            numOfItems++;
        } else {
            listItem.style.display = "none";
        }
    }
  
    if (numOfItems == 0) {
        noItemMsg.style.display = "block";
    } else {
        noItemMsg.style.display = "none";
    }

    if (this.value.length == 0) {
        document.getElementById("about_tsp_title").style.display = "block";
        document.getElementById("about_tsp_pic").style.display = "block";
        document.getElementById("about_box").style.display = "block";
        list.style.display = "none";
    }
  });