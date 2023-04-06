// Get the form and CSRF token
const form = document.querySelector('#form');
const csrf_token = form.querySelector('input[name="csrfmiddlewaretoken"]').value;

// Initialize an array to hold the selected buttons
let selectedButtons = [];

// Get all the buttons on the page
const buttons = document.querySelectorAll('button');

// Loop through each button
buttons.forEach((button) => {
  // Add a click event listener to the button
  button.addEventListener('click', (event) => {
    // Get the button's name
    event.preventDefault();
    const buttonName = event.target.innerText.trim();
    
    // Exclude the signup button from being selected
    if (buttonName === 'Sign Up') {
      return;
    }

    // Toggle the 'selected' class on the button
    event.target.classList.toggle('selected');

    // Toggle the 'selected-color' class on the button to change its color
    event.target.classList.toggle('selected-color');

    // Check if the button is selected
    if (event.target.classList.contains('selected')) {
      // Add the button's name to an array of selected buttons
      selectedButtons.push(buttonName);
    } else {
      // Remove the button's name from the array of selected buttons
      selectedButtons = selectedButtons.filter((selectedButton) => selectedButton !== buttonName);
    }
  });
});

// Add a submit event listener to the form
form.addEventListener('submit',(e) => {
  e.preventDefault();

  // Get the email id from the form
  const useremail = form.elements.email.value;

  // Create an object with the email and selected buttons
  const data = {email:useremail, choices:selectedButtons};

  // Log the data to the console
  console.log(data);

  // Cheeck if choice is empty
  if (selectedButtons.length === 0) {
    alert('Please select at least one topic');
    return;
  }

  // Send an AJAX request to save the data to the Django database
  fetch('/save_email', {
    method: 'POST', 
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrf_token
    },
    body: JSON.stringify(data)
  })
  .then(response => {
    if(!response.ok){
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    console.log('Data saved successfully:', data);
    // Reload the page and raise success alert after the data is saved
    alert('Registration Successful !!!')
    window.location.reload(); 
  })
  .catch(error => {
    console.error('Error saving data:', error);
  });
});

// Text typing effect
const heading = document.getElementById("typing-heading");
const textArr = ["W O R L D", "F I N A N C E", "T E C H N O L O G Y", "H E A L T H", "B U S I N E S S"];
let i = 0;
let j = 0;

function type() {
  if (i === textArr.length) {
    i = 0;
  }
  const currentText = textArr[i];
  if (j < currentText.length) {
    heading.innerHTML += currentText.charAt(j);
    j++;
    setTimeout(type, 50);
  } else {
    setTimeout(erase, 1000);
  }
}

function erase() {
  if (j > 0) {
    heading.innerHTML = heading.innerHTML.slice(0, -1);
    j--;
    setTimeout(erase, 50);
  } else {
    i++;
    setTimeout(type, 550);
  }
}

// Start the typing effect when the page is loaded
document.addEventListener("DOMContentLoaded", type);

//sccroll to bottom
function scrollToBottom() {
  window.scroll({
    top: document.body.scrollHeight,
    behavior: "smooth"
  });
}

