//此頁控制怪物大寶動作
//怪物控制使用dabuo控制
class dabuo extends Phaser.Physics.Arcade.Sprite {
        constructor(scene, x, y) {
            super(scene, x, y, "dabuo");
            this.scene = scene;
            scene.add.existing(this);
        }