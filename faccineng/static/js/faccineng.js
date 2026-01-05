/*document.addEventListener('DOMContentLoaded', function() {
    const navContent = document.querySelector('.nav-itens');
    const header = document.querySelector('.header');
    
    if (navContent && header) {
        const headerHeight = header.offsetHeight;
        const navHeight = navContent.offsetHeight;
        
        window.addEventListener('scroll', function() {
            const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
            
            if (scrollTop > headerHeight - navHeight) {
                navContent.classList.add('fixed');
                document.getElementById('main').style.paddingTop = navHeight + 'px';
            } else {
                navContent.classList.remove('fixed');
                document.getElementById('main').style.paddingTop = '0';
            }
        });
    }
    }); */