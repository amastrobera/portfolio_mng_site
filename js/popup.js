function show_popup(mylink, windowname) { 
	if (! window.focus){
		return true; 
	}
	var href; 
	if (typeof(mylink) == 'string') {
		href=mylink; 
	}
	else {
		href=mylink.href; 
	}
	window.open(href, windowname,'width=400,height=200,scrollbars=yes'); 
	return false; 
} 

function close_popup(mylink, closeme, closeonly) { 
	if (!(window.focus && window.opener)){
		return true; 
	}
	window.opener.focus(); 
	if (!closeonly){
		window.opener.location.href=mylink.href; 
	}
	if (closeme){
		window.close(); 
	}
	return false; 
} 




