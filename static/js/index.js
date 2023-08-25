
// ---------------------------Our news section popup-------------------

document.addEventListener('DOMContentLoaded', () => {
    const seeMoreButtons = document.querySelectorAll('.see-more-button');
    const popup = document.getElementById('popup');
    const popupImage = document.getElementById('popupImage');
    const popupTitle = document.getElementById('popupTitle');
    const popupDescription = document.getElementById('popupDescription');
    const closePopup = document.getElementById('closePopup');
    
    seeMoreButtons.forEach(button => {
        button.addEventListener('click', () => {
            const image = button.getAttribute('data-image');
            const title = button.getAttribute('data-title');
            const description = button.getAttribute('data-description');
            
            popupImage.src = image;
            popupTitle.textContent = title;
            popupDescription.textContent = description;
            
            popup.style.display = 'block';
        });
    });
    
    closePopup.addEventListener('click', () => {
        popup.style.display = 'none';
    });
    
    window.addEventListener('click', (event) => {
        if (event.target === popup) {
            popup.style.display = 'none';
        }
    });
});


