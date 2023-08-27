
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
let toggleClass = "is-sticky";
let inactive = "inactive";

window.addEventListener("scroll", () => {
  const currentScroll = window.scrollY;
  if (currentScroll > 100) {
    header.classList.add(toggleClass);
    header.classList.remove(inactive);
  } else {
    header.classList.add(inactive);
    header.classList.remove(toggleClass);
  }
  animation('.slide-wraper-right')
  animation('.slide-wraper-left')
  animation('.wraper-animated')
});

function animation(claslist) {
    let slideWrappers = document.querySelectorAll(claslist);
    let threshold = 100; // Adjust this threshold as needed
    slideWrappers.forEach(slideWrapper => {
        let triggerPosition = slideWrapper.getBoundingClientRect().top;
        if (triggerPosition < threshold) {
            slideWrapper.classList.add('active');
        } else {
            slideWrapper.classList.remove('active');
        }
    });
  }
