document.addEventListener('DOMContentLoaded', function() {
    const nav = document.querySelector('nav');
    const header = document.querySelector('header');
    
    if (nav && header) {
        const banner = document.getElementById('rotating-banner');
        const bannerHeight = banner ? banner.offsetHeight: 0;
        
        window.addEventListener('scroll', function() {
            const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
            
            if (scrollTop > bannerHeight) {
                nav.classList.add('fixed');
                header.style.paddingBottom = nav.offsetHeight + 'px';
            } else {
                nav.classList.remove('fixed');
                header.style.paddingBottom = '0';
            }
        });
    }
    }); 