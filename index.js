const btn = document.getElementById('btn');

btn.addEventListener('click', () => {
  const form = ("Contact-us.html").getElementById("contact-form");

  if (form.style.visibility === 'hidden') {
    form.style.visibility = 'visible';
  } else {
    form.style.visibility = 'hidden';
  }
});