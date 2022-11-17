window.onload=function(){
	$('#popoverData1').popover(
		{html:true}
	);
	$('#popoverData2').popover(
		{html:true}
	);
	$('#popoverData3').popover(
		{html:true}
	);

	$("#met7-bt").click(function(event){
		let message = {
		}
		$.post("http://127.0.0.1:3000/predict7", JSON.stringify(message), function(response){
			base = response.img1;
			met1_1.setAttribute('src', "data:image/jpg;base64," + base);
			base = response.img2;
			met1_2.setAttribute('src', "data:image/jpg;base64," + base);
			base = response.img3;
			met1_3.setAttribute('src', "data:image/jpg;base64," + base);
			base = response.img4;
			met1_4.setAttribute('src', "data:image/jpg;base64," + base);
			base = response.img5;
			met1_5.setAttribute('src', "data:image/jpg;base64," + base);
		});
	});

	$("#met1-bt").click(function(event){
		let message = {
		}
		$.post("http://127.0.0.1:3000/predict1", JSON.stringify(message), function(response){
			base = response.img1;
			met1_1.setAttribute('src', "data:image/jpg;base64," + base);
			base = response.img2;
			met1_2.setAttribute('src', "data:image/jpg;base64," + base);
			base = response.img3;
			met1_3.setAttribute('src', "data:image/jpg;base64," + base);
			base = response.img4;
			met1_4.setAttribute('src', "data:image/jpg;base64," + base);
			base = response.img5;
			met1_5.setAttribute('src', "data:image/jpg;base64," + base);
		});
	});

	$("#met2-bt").click(function(event){
		let message = {
		}
		$.post("http://127.0.0.1:3000/predict2", JSON.stringify(message), function(response){
			base = response.img1;
			met2_1.setAttribute('src', "data:image/jpg;base64," + base);
			base = response.img2;
			met2_2.setAttribute('src', "data:image/jpg;base64," + base);
			base = response.img3;
			met2_3.setAttribute('src', "data:image/jpg;base64," + base);
			base = response.img4;
			met2_4.setAttribute('src', "data:image/jpg;base64," + base);
			base = response.img5;
			met2_5.setAttribute('src', "data:image/jpg;base64," + base);
		});
	});

	$("#met3-bt").click(function(event){
		let message = {
		}
		$.post("http://127.0.0.1:3000/predict3", JSON.stringify(message), function(response){
			base = response.img1;
			met3_1.setAttribute('src', "data:image/jpg;base64," + base);
			base = response.img2;
			met3_2.setAttribute('src', "data:image/jpg;base64," + base);
			base = response.img3;
			met3_3.setAttribute('src', "data:image/jpg;base64," + base);
			base = response.img4;
			met3_4.setAttribute('src', "data:image/jpg;base64," + base);
			base = response.img5;
			met3_5.setAttribute('src', "data:image/jpg;base64," + base);
		});
	});

	$("#met4-bt").click(function(event){
		let message = {
		}
		$.post("http://127.0.0.1:3000/predict4", JSON.stringify(message), function(response){
			base = response.img1;
			met1_1.setAttribute('src', "data:image/jpg;base64," + base);
			base = response.img2;
			met1_2.setAttribute('src', "data:image/jpg;base64," + base);
			base = response.img3;
			met1_3.setAttribute('src', "data:image/jpg;base64," + base);
			base = response.img4;
			met1_4.setAttribute('src', "data:image/jpg;base64," + base);
			base = response.img5;
			met1_5.setAttribute('src', "data:image/jpg;base64," + base);
		});
	});

	$("#met5-bt").click(function(event){
		let message = {
		}
		$.post("http://127.0.0.1:3000/predict5", JSON.stringify(message), function(response){
			base = response.img1;
			met2_1.setAttribute('src', "data:image/jpg;base64," + base);
			base = response.img2;
			met2_2.setAttribute('src', "data:image/jpg;base64," + base);
			base = response.img3;
			met2_3.setAttribute('src', "data:image/jpg;base64," + base);
			base = response.img4;
			met2_4.setAttribute('src', "data:image/jpg;base64," + base);
			base = response.img5;
			met2_5.setAttribute('src', "data:image/jpg;base64," + base);
		});
	});

	$("#met6-bt").click(function(event){
		let message = {
		}
		$.post("http://127.0.0.1:3000/predict6", JSON.stringify(message), function(response){
			base = response.img1;
			met3_1.setAttribute('src', "data:image/jpg;base64," + base);
			base = response.img2;
			met3_2.setAttribute('src', "data:image/jpg;base64," + base);
			base = response.img3;
			met3_3.setAttribute('src', "data:image/jpg;base64," + base);
			base = response.img4;
			met3_4.setAttribute('src', "data:image/jpg;base64," + base);
			base = response.img5;
			met3_5.setAttribute('src', "data:image/jpg;base64," + base);
		});
	});
};

$(function() {

    $('#met1').click(function(e) {
		$('#met2').removeClass('active');
		$('#met3').removeClass('active');
		$('#met4').removeClass('active');
		$('#met5').removeClass('active');
		$('#met6').removeClass('active');
		$('#met7').removeClass('active');
		$(this).addClass('active');
		
		$('#met1-b').removeClass('hidden');
		$('#met2-b').addClass('hidden');
		$('#met3-b').addClass('hidden');
		$('#met4-b').addClass('hidden');
		$('#met5-b').addClass('hidden');
		$('#met6-b').addClass('hidden');
		$('#met7-b').addClass('hidden');
		
		e.preventDefault();
	});
	$('#met2').click(function(e) {
		$('#met1').removeClass('active');
		$('#met3').removeClass('active');
		$('#met4').removeClass('active');
		$('#met5').removeClass('active');
		$('#met6').removeClass('active');
		$('#met7').removeClass('active');
		$(this).addClass('active');
		
		$('#met2-b').removeClass('hidden');
		$('#met1-b').addClass('hidden');
		$('#met3-b').addClass('hidden');
		$('#met4-b').addClass('hidden');
		$('#met5-b').addClass('hidden');
		$('#met6-b').addClass('hidden');
		$('#met7-b').addClass('hidden');
		
		e.preventDefault();
	});
	$('#met3').click(function(e) {
		$('#met2').removeClass('active');
		$('#met1').removeClass('active');
		$('#met4').removeClass('active');
		$('#met5').removeClass('active');
		$('#met6').removeClass('active');
		$('#met7').removeClass('active');
		$(this).addClass('active');
		
		$('#met3-b').removeClass('hidden');
		$('#met2-b').addClass('hidden');
		$('#met1-b').addClass('hidden');
		$('#met4-b').addClass('hidden');
		$('#met5-b').addClass('hidden');
		$('#met6-b').addClass('hidden');
		$('#met7-b').addClass('hidden');
		
		e.preventDefault();
	});
});