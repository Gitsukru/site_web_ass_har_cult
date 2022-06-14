//Navbar active link add class in css 
const activePage = window.location.pathname;
const navLinks = document.querySelectorAll('.nav-item a').forEach(link => {
    if ((link.href.includes(`${activePage}`) && activePage !== "/") || (activePage == "/" && link.id == "accueil")) {
        link.classList.add('active');
    }
});

let mybutton = document.getElementById("backTotopbtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () {
    scrollFunction()
};

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        mybutton.style.display = "block";
    } else {
        mybutton.style.display = "none";
    }
}

function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}