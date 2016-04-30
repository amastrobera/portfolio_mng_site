function show_popup(mylink, windowname, data) { 
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
	window.open(href, windowname,
	        'top=200,left=500,width=600,height=400,scrollbars=yes'); 
	if (data){
	    alert(data);
	    var dObj = JSON.load(data);
	    window.data = dObj;
	}
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




