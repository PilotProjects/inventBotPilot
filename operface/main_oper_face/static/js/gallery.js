document.addEventListener('DOMContentLoaded', onDomReady, false);

function onDomReady()
{
    var links = document.getElementsByClassName('toggle_img');
    for (var i = 0; i < links.length; i++)
    {
        var thisLink = links[i];
        thisLink.addEventListener("click", function()
        {
            handleLinkClick(event, thisLink);
        });
    }
}

function handleLinkClick(event, link)
{
    var currentSrc = link.href;
    var toggleSrc = link.getAttribute("data-img");
    var img = link.getElementsByTagName('img')[0];
    img.src = toggleSrc;
    link.href = toggleSrc;
    link.setAttribute("data-img", currentSrc);
    event.preventDefault();
}
