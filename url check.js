// More API functions here:
// https://github.com/googlecreativelab/teachablemachine-community/tree/master/libraries/image
// the link to your model provided by Teachable Machine export panel
let model, webcam, labelContainer, maxPredictions;
URL = 'https://teachablemachine.withgoogle.com/models/R7w-4iuPa/';
// Load the image model and setup the webcam
async function init() {
    const modelURL = URL + 'model.json';
    const metadataURL = URL + 'metadata.json';

    // load the model and metadata
    // Refer to tmImage.loadFromFiles() in the API to support files from a file picker
    // or files from your local hard drive
    // Note: the pose library adds "tmImage" object to your window (window.tmImage)
    model = await tmImage.load(modelURL, metadataURL);
    maxPredictions = model.getTotalClasses();
    labelContainer = document.getElementById('label-container');
    for (let i = 0; i < maxPredictions; i++) {
        // and class labels
        labelContainer.appendChild(document.createElement('div'));
    }
}

// run the webcam image through the image model
async function predict() {
    // predict can take in an image, video or canvas html element
    var image = document.getElementById('face-image');
    const prediction = await model.predict(image, false);
    prediction.sort((a, b) => parseFloat(b.probability) - parseFloat(a.probability));
    switch (prediction[0].className) {
        case 'Nami':
            resultMessage = '나미';
            break;
        case 'Gayoung':
            resultMessage = '가영';
            break;
        case 'Sawako':
            resultMessage = '사와코';
            break;
        case 'Sakura':
            resultMessage = '사쿠라';
            break;
        case 'Elsa':
            resultMessage = '엘사';
            break;
        case 'Mi ran':
            resultMessage = '미란이';
            break;
        case 'Conan':
            resultMessage = '남도일';
            break;
        case 'Inuyasha':
            resultMessage = '이누야샤';
            break;
        case 'Naruto':
            resultMessage = '나루토';
            break;
        case 'Loopy':
            resultMessage = '루피';
            break;
        case 'Kazehaya Shota':
            resultMessage = '카제하야 쇼타';
            break;
        case 'Son Okong':
            resultMessage = '손오공';
            break;
    }
    $('.result-message').html(resultMessage);
    for (let i = 0; i < maxPredictions; i++) {
        const classPrediction =
            prediction[i].className + ': ' + prediction[i].probability.toFixed(2);
        labelContainer.childNodes[i].innerHTML = classPrediction;
    }
}
function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('.image-upload-wrap').hide();

            $('.file-upload-image').attr('src', e.target.result);
            $('.file-upload-content').show();

            $('.image-title').html(input.files[0].name);
        };

        reader.readAsDataURL(input.files[0]);
        if (document.getElementById('checkbox_status').checked == true) {
            console.log(document.getElementById('checkbox_status').checked);
            URL = 'https://teachablemachine.withgoogle.com/models/lL7xnVuac/';
            init().then(() => {
                predict();
            });
        } else {
            console.log(document.getElementById('checkbox_status').checked);
            URL = 'https://teachablemachine.withgoogle.com/models/R7w-4iuPa/';
            document.querySelector('.loadingio-spinner-spinner-kznotoksuti').style.cssText =
                'display:inline-block';
            init().then(() => {
                predict();
                document.querySelector('.loadingio-spinner-spinner-kznotoksuti').style.cssText =
                    'display:none';
                document.querySelector('.addthis_inline_share_toolbox').style.cssText =
                    'display:inline';
            });
        }
    } else {
        removeUpload();
    }
}

function removeUpload() {
    $('.file-upload-input').replaceWith($('.file-upload-input').clone());
    $('.file-upload-content').hide();
    $('.image-upload-wrap').show();
}
$('.image-upload-wrap').bind('dragover', function () {
    $('.image-upload-wrap').addClass('image-dropping');
});
$('.image-upload-wrap').bind('dragleave', function () {
    $('.image-upload-wrap').removeClass('image-dropping');
});