//此頁控制菩薩動作
//菩薩控制使用pusa控制
class pusa extends Phaser.Physics.Arcade.Sprite {
        constructor(scene, x, y) {
            super(scene, x, y, "pusa");
            this.scene = scene;
            scene.add.existing(this);
        }