let searchBar = document.getElementById("search");
let list = document.getElementById("list");

searchBar.addEventListener("input", function() {
  let searchTerm = searchBar.value.toLowerCase();
  let listItems = list.getElementsByClassName("list_item");
  let noItemMsg = document.getElementById("NoItemMsg");
  let numOfItems = 0;
  document.getElementsByTagName("h2")[0].style.display = "none";
  document.getElementsByClassName("Store_Container")[0].style.display = "none";
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
    document.getElementsByTagName("h2")[0].style.display = "block";
    document.getElementsByClassName("Store_Container")[0].style.display = "block";
    list.style.display = "none";
  }
});
