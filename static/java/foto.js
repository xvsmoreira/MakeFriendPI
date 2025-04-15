	const fotoInput = document.querySelector('#foto');
const fotoPreview = document.querySelector('#foto-preview');

fotoInput.addEventListener('change', () => {
  const file = fotoInput.files[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = () => {
      fotoPreview.src = reader.result;
    };
    reader.readAsDataURL(file);
  }
});

