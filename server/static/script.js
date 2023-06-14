document.addEventListener('DOMContentLoaded', function() {
    const activePage = window.location.pathname;
    const navLinks = document.querySelectorAll('nav a')
    .forEach(link => {
        if(link.href.includes(`${activePage}`)){
            link.classList.add('active');
        }
    })
});

function reloadIframe(){
    var iframe = document.getElementById('data-lens');
    iframe.src = iframe.src;
}