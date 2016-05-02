function show_popup(mylink, windowname, data)
{ 
    alert("show popup");
	if (! window.focus)
	{
	    alert("not window focus");
		return false; 
	}
	var href; 
	if (typeof(mylink) == 'string')
	{
	    alert("string: " + mylink);
		href=mylink; 
	}
	else
	{
	    alert("mylink is href" + String(mylink.href));
		href=mylink.href; 
	}
	window.open(href, windowname,
	        'top=200,left=500,width=600,height=400,scrollbars=yes'); 
	if (data)
	{
	    var dObj = JSON.parse(data);
	    var ud = document.createAttribute("userData");
	    ud.value = dObj;
	}
	return true; 
} 

function close_popup(mylink, closeme, closeonly)
{ 
	if (!(window.focus && window.opener))
	{
		return false; 
	}
	window.opener.focus(); 
	if (!closeonly)
	{
		window.opener.location.href=mylink.href; 
	}
	if (closeme)
	{
		window.close(); 
	}
	return true; 
} 




