(function () {
	const response = {
		"type": "page",
		"body": [
		  {
			"type": "form",
			"title": "表单",
			"body": [
				{
					"type": "editor",
					"label": "代码编辑器",
					"name": "editor"
				}
			],
			"api": {
			  "method": "post",
			  "url": "/api/load_data",
			  "dataType": "json"
			},
		  }
		],
		"aside": [
		],
		"messages": {
		},
		"pullRefresh": {
		}
	}
	window.jsonpCallback && window.jsonpCallback(response);
})();
