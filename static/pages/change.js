(function () {
    const response = {
        "type": "page",
        "body": [
            {
                "type": "input-tree",
                "label": "树选择框",
                "name": "tree",
                "options": [
                    {
                        "label": "选项A",
                        "value": "A",
                        "children": [
                            {
                                "label": "选项C",
                                "value": "C"
                            },
                            {
                                "label": "选项D",
                                "value": "D"
                            }
                        ]
                    },
                    {
                        "label": "选项B",
                        "value": "B"
                    }
                ],
                "id": "u:831c13cd9f30"
            },
            {
                "type": "qrcode",
                "value": "https://amis.baidu.com",
                "id": "u:64cd1fb811d0"
            }
        ],
        "aside": [
        ],
        "id": "u:88d018dfd973",
        "messages": {
        },
        "pullRefresh": {
        }
    }
    window.jsonpCallback && window.jsonpCallback(response);
})();
