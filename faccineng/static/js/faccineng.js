document.addEventListener('DOMContentLoaded', function() {
    const nav = document.querySelector('nav');
    const header = document.querySelector('header');
    const main = document.querySelector('main') || document.querySelector('#main') || document.body;
    
    if (nav && header) {
        const banner = document.getElementById('rotating-banner');
        const bannerHeight = banner ? banner.offsetHeight: 0;
        let navHeight = nav.offsetHeight;
        
        window.addEventListener('scroll', function() {
            const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
            
            if (scrollTop > bannerHeight) {
                if (!nav.classList.contains('fixed')){
                    nav.classList.add('fixed');
                    main.style.paddingTop = navHeight + 'px';
                }
            } else {
                if (nav.classList.contains('fixed')){
                nav.classList.remove('fixed');
                main.style.paddingTop = '0';
            }
        }
        });
    }
    }); 