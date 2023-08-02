// a JavaScript script that adds a <li> element to a list when the user clicks on the tag DIV#add_item:
// The new element must be <li>Item</li> and must be added to UL.my_list

$('div#add_item').click(function () {
	let new_element = '<li>Item</li>';
	$('ul.my_list').append(new_element);
});
