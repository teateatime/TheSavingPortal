function burgerMenu() {
    let menu = document.getElementById("myDropdown");
    if (menu.style.display === "none") {
        menu.style.display = "block";
    } else {
        menu.style.display = "none";
    }
}

function toggleMenu(elementId) {
    let ID1 = "HomeLnk";
    let ID2 = "AboutWeb";
    let menu = document.getElementById("myDropdown");
    if (elementId === ID1) {
        menu.style.display = "none";
    } else if (elementId === ID2) {
        menu.style.display = "none";
    }
}

window.onclick = function(event) {
    if (!event.target.matches('.bar')) {
        let menu = document.getElementById("myDropdown");

        if (menu.style.display === "block") {
            menu.style.display = "none";
        }
    }
}
