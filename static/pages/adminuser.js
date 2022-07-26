(function () {
	const response = {
		"type": "page",
		"body": [
			{
				"label": "新增",
				"type": "button",
				"actionType": "dialog",
				"level": "primary",
				"className": "m-b-sm",
				"dialog": {
					"title": "新增表单",
					"body": {
						"type": "form",
						"body": [
							{
								"label": "邮箱",
								"type": "input-email",
								"name": "email",
								"id": "u:d42392766334",
								"validations": {
								},
								"validationErrors": {
								}
							},
							{
								"type": "input-password",
								"label": "密码",
								"name": "password",
								"id": "u:d1b360d8b947",
								"showCounter": false,
								"required": true
							}
						],
						"api": {
							"method": "post",
							"url": "/api/users/",
							"dataType": "json"
						}
					}
				}
			},
			{
				"type": "crud",
				"api": "/api/users/",
				"syncLocation": false,
				"columns": [
					{
						"name": "id",
						"label": "ID"
					},
					{
						"name": "email",
						"label": "邮箱"
					},
					{
						"name": "is_active",
						"label": "是否激活"
					},
					{
						"type": "operation",
						"label": "操作",
						"buttons": [
							{
								"label": "修改",
								"type": "button",
								"level": "link",
								"actionType": "drawer",
								"drawer": {
								  "title": "修改用户数据",
								  "body": {
									"type": "form",
									"initApi": "/api/users/${id}",
									"api": "put:/api/users/${id}",
									"body": [
										{
											"label": "邮箱",
											"type": "input-email",
											"name": "email"
										},
										{
											"type": "input-password",
											"label": "密码",
											"name": "password",
											"showCounter": false,
											"required": true
										}
									]
								  }
								}
							},
							{
								"label": "删除",
								"type": "button",
								"actionType": "ajax",
								"level": "link",
								"confirmText": "确认要删除？",
								"api": "delete:/api/users/${id}"
							}
						]
					}
				]
			}
		]
	}
	window.jsonpCallback && window.jsonpCallback(response);
})();
