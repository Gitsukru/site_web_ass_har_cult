//Navbar active link add class in css 
const activePage = window.location.pathname;
const navLinks = document.querySelectorAll('.nav-item a').forEach(link => {
    if ((link.href.includes(`${activePage}`) && activePage !== "/") || (activePage == "/" && link.id == "accueil")) {
        link.classList.add('active');
    }
});