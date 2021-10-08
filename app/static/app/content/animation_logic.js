const AnimItems = document.querySelectorAll('._anim_items');

if (AnimItems.length > 0) {
    window.addEventListener('scroll', AnimOnScroll)
    function AnimOnScroll() {
        for (let index = 0; index < AnimItems.length; index++) {
            const AnimItem = AnimItems[index];
            const AnimItemHeight = AnimItem.offsetHeight;
            const AnimItemOffset = offset(AnimItem).top;
            const AnimStart = 4;

            let AnimItemPoint = window.innerHeight - AnimItemHeight / AnimStart;

            if (AnimItemHeight > window.innerHeight) {
                AnimItemPoint = window.innerHeight - AnimItemHeight / AnimStart;
            }

            if ((scrollY > AnimItemOffset - AnimItemPoint) && scrollY < (AnimItemOffset + AnimItemHeight)) {
                AnimItem.classList.remove('innact_anim')
                AnimItem.classList.add('act_anim');
            } else {
                if (!AnimItem.classList.contains('_anim_no_hide'))
                {
                    AnimItem.classList.remove('act_anim');
                    AnimItem.classList.add('innact_anim')
                }
            }
        }
    }
    function offset(el) {
        const rect = el.getBoundingClientRect(),
            scrollLeft = window.pageXOffset || document.documentElement.scrollLeft,
            scrollTop = window.scrollY || document.documentElement.scrollTop;
        return { top: rect.top + scrollTop, left: rect.left + scrollLeft }
    }

    setTimeout(() => {
        AnimOnScroll();
    }, 500);
}