var app = angular.module('myapp', []);
app.controller('myctl', function($scope, $http){
			/*
			$scope.startdate = "testtttt";
			$scope.enddate = "tttttttttest";
			$scope.query = function(){
				$scope.period = "from "+$scope.startdate+" to "+$scope.enddate;
			};
			$scope.query();
			
			$http.get("http://192.168.56.101:8090/dynatag/api/configuration").then(function(response){
				
				$scope.applications = response.data.application;
				
			}, function(response){
				$scope.error = "There are something error!"
			});
			*/
	
			$scope.query = function(){
				$http({
					method:"GET",
					url:"http://192.168.56.101:8090/dynatag/api/configurations"
				}).then(function successCallback(response){
					$scope.configurations = response.data.results;
				}, function errorCallback(response){
					$scope.error = "There are something error!"
				});
			};
			$scope.query();
});


app.controller('appctl', function($scope, $window){
	
	$scope.registerinfusion = function(){
		
		url = 'https://signin.infusionsoft.com/app/oauth/authorize';
		url = url + '?client_id=' + $scope.client_id;
		url = url + '&redirect_uri=' + $scope.redirect_url + 'add/';
		url = url + '&response_type=' + $scope.response_type;
		url = url + '&scope=full';
		//console.log(decodeURI('https://mytest.com/abc?code=vtu7ckj73e7muhnat9zebafd&scope=full%7Caa331.infusionsoft.com&state='));
		
		$window.open(encodeURI(url), "popup", "width=500,height=500,left=10,top=150");
		
	};
	
});




