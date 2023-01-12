let rateSearchBar = document.getElementById("rate_search");
let list = document.getElementById("list");

rateSearchBar.addEventListener("input", function() {
    let searchTerm = rateSearchBar.value.toLowerCase();
    let listItems = list.getElementsByClassName("list_item");
    let noItemMsg = document.getElementById("NoItemMsg");
    let numOfItems = 0;
    document.getElementById("store_title").style.display = "none";
    document.getElementsByClassName("chart-container")[0].style.display = "none";
    document.getElementsByClassName("Providers_Table")[0].style.display = "none";
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
        document.getElementById("store_title").style.display = "block";
        document.getElementsByClassName("chart-container")[0].style.display = "block";
        document.getElementsByClassName("Providers_Table")[0].style.display = "table";
        list.style.display = "none";
    }
  });