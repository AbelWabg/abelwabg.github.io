//此頁控制背景
//背景控制sc2
class scene extends Phaser.Scene {
    constructor() {
            super({ key: "scene" });
        }
        //預先載入場景
    preload() {

        this.load.image("dabuo", 'assets/dabuo.png');
        this.load.image("stick", 'assets/stick.png');
        this.load.image("kycg", 'assets/KYCG.png');
        this.load.image("pusa", "assets/pusa.png");
    }

    //創建畫面

    create() {

        this.add.image(400, 70, 'dabuo');
        this.add.image(370, 520, 'stick');
        this.add.image(400, 460, 'kycg');


        //設置文本
        const text2 = this.add.text(30, 30, '', { font: '16px Courier', fill: '#00ff00' });



        //設定菩薩背景
        const pusa = this.add.image(400, 550, 'pusa');

        //  Store some data about this Gem:
        pusa.setDataEnabled();

        //  Whenever a data value is first set it will dispatch a setdata event
        pusa.on('setdata', function(gameObject, key, value) {
            list.push(key);
            text2.setText(list);
        });




        //  Whenever a data value is updated it will dispatch a changedata event
        pusa.on('changedata', function(gameObject, key, value) {
            text2.setText([
                '關卡: ' + pusa.data.get('關卡'),
                '等級: ' + pusa.data.get('等級') + ' 等級',
                '怒氣: ' + pusa.data.get('怒氣') + ' 怒氣',
            ]);

        });

        //  Change the 'value' property when the mouse is clicked
        this.input.on('pointerdown', function() {
            const 怒氣 = pusa.data.get('怒氣');
            const 等級 =pusa.data.get('等級');
            
            if (!怒氣) {
                //  Set the value, this will emit the `setdata` and `changedata` events

                pusa.data.set('怒氣', 50);

                text2.setText([
                    '關卡: ' + pusa.data.get('關卡'),
                    '等級: ' + pusa.data.get('等級'),
                    '怒氣: ' + pusa.data.get('怒氣') + ' 怒氣',
                ]);
            } else {
                //  Set the value, this will call the 'after' callback
                pusa.data.set('怒氣', 怒氣 + 50);
            }

        });
    }


    //動作聲明

    update() {



    }
}