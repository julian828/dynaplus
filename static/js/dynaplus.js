var app = angular.module('myapp', []);
app.controller('myctl', function($scope){
			$scope.startdate = "testtttt";
			$scope.enddate = "tttttttttest";
			$scope.query = function(){
				$scope.period = "from "+$scope.startdate+" to "+$scope.enddate;
			};
			$scope.query();
		});