function generate_random_string(string_length) {
    var random_string = '';
    var random_ascii;
    for(var  i = 0; i < string_length; i++) {
        random_ascii = Math.floor((Math.random() * 25) + 97);
        random_string += String.fromCharCode(random_ascii)
    }
    return random_string
}