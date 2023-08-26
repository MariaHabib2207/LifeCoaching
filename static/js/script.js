
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
            popupImage.src = baseUrl +image;
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



const header = document.querySelector(".page-header");
const toggleClass = "is-sticky";

window.addEventListener("scroll", () => {
  const currentScroll = window.scrollY;
  console.log(currentScroll); 
  if (currentScroll > 100) {
    header.classList.add(toggleClass);
  } else {
    header.classList.remove(toggleClass);
  }
});
