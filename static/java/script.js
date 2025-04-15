let count =1;
	document.getElementById("radio1").checked = true;

setInterval( function(){
		nextImage();
}, 3000)


function nextImage(){
	count++;
	if(count>4){
		count=1;
	}
document.getElementById("radio"+count).checked = true;
}

const form = document.getElementById('animal-form');

form.addEventListener('submit', function(event) {
    event.preventDefault(); 
    sendDataToServer(); 
    alert('Animal cadastrado com sucesso!');
    const messageElement = document.getElementById('confirmation-message');
    messageElement.innerHTML = 'Animal cadastrado com sucesso!';
});