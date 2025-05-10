document.addEventListener('DOMContentLoaded', () => {
    // Smooth Scroll for internal links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Toggle details of each mission point
    const missionHeadings = document.querySelectorAll('.mission-content h3');
    missionHeadings.forEach(heading => {
        heading.addEventListener('click', () => {
            const nextElement = heading.nextElementSibling;
            nextElement.classList.toggle('hidden');
            heading.classList.toggle('active');
        });
    });

    // Add smooth animation to member hover effect
    const members = document.querySelectorAll('.member');
    members.forEach(member => {
        member.addEventListener('mouseover', () => {
            member.style.transition = 'transform 0.3s ease, box-shadow 0.3s ease';
        });
        member.addEventListener('mouseout', () => {
            member.style.transition = 'transform 0.3s ease, box-shadow 0.3s ease';
        });
    });

    // Toggle light/dark mode
    const toggleButton = document.getElementById('toggle-theme');
    toggleButton.addEventListener('click', () => {
        document.body.classList.toggle('dark-mode');
        toggleButton.textContent = document.body.classList.contains('dark-mode') ? 'Light Mode' : 'Dark Mode';
    });
});