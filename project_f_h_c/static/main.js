// const scrollSpy = new bootstrap.ScrollSpy(document.body, {
//     target: '#navbar-example'
// })

// console.log(scrollSpy);
// function formatPhoneNumber(value) {
//     if (!value) return value;
//     const phoneNumber = value.replace(/[^\d]/g, '');
//     const phoneNumberLenght = phoneNumber.length;
//     if (phoneNumberLenght < 4) return phoneNumber;
//     if (phoneNumberLenght < 7) {
//         return `(${phoneNumber.slice(0,3)}) ${phoneNumber.slice(3)}`;
//     }
//     return `(${phoneNumber.slice(0,3)}) ${phoneNumber.slice(3,6)} ${phoneNumber.slice(7,8)} ${phoneNumber.slice(9,10)}`;
// }

// function phoneNumberFormatter() {
//     const inputField = document.getElementById('phone_number');
//     const formattedInputValue = formatPhoneNumber(inputField.value);
//     inputField.value = formattedInputValue;
// }

// phoneNumberFormatter()


// function formatPhoneNumber(phoneNumberString) {
//     var cleaned = ('' + phoneNumberString).replace(/\D/g, '');
//     var match = cleaned.match(/^(1|)?(\d{3})(\d{3})(\d{4})$/);
//     if (match) {
//       var intlCode = (match[1] ? '+1 ' : '');
//       return [intlCode, '(', match[2], ') ', match[3], '-', match[4]].join('');
//     }
//     return null;
//   }




// const isNumericInput = (event) => {
//     const key = event.keyCode;
//     return ((key >= 48 && key <= 57) || // Allow number line
//         (key >= 96 && key <= 105) // Allow number pad
//     );
// };

// const isModifierKey = (event) => {
//     const key = event.keyCode;
//     return (event.shiftKey === true || key === 35 || key === 36) || // Allow Shift, Home, End
//         (key === 8 || key === 9 || key === 13 || key === 46) || // Allow Backspace, Tab, Enter, Delete
//         (key > 36 && key < 41) || // Allow left, up, right, down
//         (
//             // Allow Ctrl/Command + A,C,V,X,Z
//             (event.ctrlKey === true || event.metaKey === true) &&
//             (key === 65 || key === 67 || key === 86 || key === 88 || key === 90)
//         )
// };

// const enforceFormat = (event) => {
//     // Input must be of a valid number format or a modifier key, and not longer than ten digits
//     if (!isNumericInput(event) && !isModifierKey(event)) {
//         event.preventDefault();
//     }
// };

// const formatToPhone = (event) => {
//     if (isModifierKey(event)) {
//         return;
//     }

//     // I am lazy and don't like to type things more than once
//     const target = event.target;
//     const input = target.value.replace(/\D/g, '').substring(0, 12); // First ten digits of input only
//     const areaCode = input.substring("+", 2);
//     const middle = input.substring(3, 6);
//     const last = input.substring(6, 10);

//     if (input.length > 6) {
//         target.value = `(${areaCode}) ${middle} - ${last}`;
//     } else if (input.length > 3) {
//         target.value = `(${areaCode}) ${middle}`;
//     } else if (input.length > 0) {
//         target.value = `(${areaCode}`;
//     }
// };

// const inputElement = document.getElementById('phone_number');
// inputElement.addEventListener('keydown', enforceFormat);
// inputElement.addEventListener('keyup', formatToPhone);