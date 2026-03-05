const squad = document.getElementById('squad');
const monitors = document.querySelectorAll('.monitor');
let currentHover = '';
monitors.forEach(mon => {
    mon.addEventListener('mouseenter', () => {
    squad.classList.add('hover-active');
    const pos = mon.classList.contains('monitor-leftmost') ? 'leftmost' :
                mon.classList.contains('monitor-left')     ? 'left' :
                mon.classList.contains('monitor-right')    ? 'right' :
                mon.classList.contains('monitor-rightmost')? 'rightmost' : '';
    currentHover = `hover-${pos}`;
    if (currentHover) squad.classList.add(currentHover);
    });

    mon.addEventListener('mouseleave', () => {
    squad.classList.remove('hover-active');
    if (currentHover) squad.classList.remove(currentHover);
    currentHover = '';
    });
});

