$(document).ready(function() {
// Porgress Bar JS  //
    $('.progress .progress-bar').each(function () {
	    var $this = $(this);
		var width = $(this).data('percent');
		$this.css({
			'transition': 'width 3s'
		});
		setTimeout(function () {
			$this.appear(function () {
				$this.css('width', width + '%');
			});
		}, 500);
    });
});