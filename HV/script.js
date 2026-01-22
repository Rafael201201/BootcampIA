function downloadPDF(){

    const element = document.querySelector('#pdf-content');
    /* console.log(element); */
    
    const otp = {
        margin: [-12, 5, -12, 5], //[arriba, izquierda, abajo, derecha] en milimetros
        filename: 'HV_Rafael_García_Sánchez.pdf',
        image: { type: 'jpeg', quality: 1 },
        html2canvas:{
            scale: 2,
            useCORS: true,
            scrollY:0
        },
        jsPDF:{
            unit: 'mm',
            format: 'a4',
            orientation: 'portrait' //Orientacion vertical
        }
    }
    html2pdf().set(otp).from(element).save();

}