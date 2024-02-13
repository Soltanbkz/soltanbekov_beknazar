document.addEventListener("DOMContentLoaded", function() {
    const burgerIcon = document.querySelector('.mobile-menu');
    const mobileNav = document.querySelector('.mobile-nav');

    // Открываем/закрываем меню при клике на иконку бургера
    burgerIcon.addEventListener('click', function() {
        mobileNav.classList.toggle('closed-menu');
    });

    // Закрываем меню при клике вне его области
    document.addEventListener('click', function(event) {
        if (!mobileNav.contains(event.target) && !burgerIcon.contains(event.target)) {
            mobileNav.classList.add('closed-menu');
        }
    });

    // Закрываем меню при клике на ссылку внутри меню
    mobileNav.querySelectorAll('a').forEach(function(link) {
        link.addEventListener('click', function() {
            mobileNav.classList.add('closed-menu');
        });
    });

    // Закрываем меню при клике на элементы с классом mobile-burgermenu
    mobileNav.querySelectorAll('.mobile-burgermenu').forEach(function(item) {
        item.addEventListener('click', function() {
            mobileNav.classList.add('closed-menu');
        });
    });
});
