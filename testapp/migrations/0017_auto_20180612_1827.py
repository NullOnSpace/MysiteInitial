# Generated by Django 2.0.4 on 2018-06-12 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0016_gift_hititv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='bid',
            field=models.IntegerField(choices=[(1, '17丷'), (2, '401'), (3, '猪芳芳'), (4, '马蚤'), (5, '驴酱灬'), (6, '雙馬尾'), (7, '安神'), (8, '小僵尸'), (9, '大帅熊'), (10, '憨厚哒'), (11, '大官'), (12, 'YJJ'), (13, '张大仙'), (14, '女流'), (15, '196'), (16, '辣椒儿'), (17, 'Np虚'), (18, '小痒虫'), (19, '小人参'), (20, 'Sao狐'), (21, '蘑菇'), (22, '寅子'), (23, '雪美眉'), (24, '二珂'), (25, '樱圆圆'), (26, '菠咕咕'), (27, '全针'), (28, '突突突'), (29, '呆妹儿'), (30, '嘉年华'), (31, '飞儿'), (32, '小便当'), (33, '猫腻'), (34, '鱼乐'), (35, '集团军'), (36, '小豆包'), (37, '一发'), (38, 'lol'), (40, '大司马'), (46, 'XDD'), (3403, '嗨宝'), (3404, '张大仙'), (3405, '软甜佳'), (3406, '大真理'), (3407, '骚白'), (3408, '正直'), (3409, '拖米'), (3410, 'AG47'), (3411, '牛头胜'), (3412, '青山丶'), (3413, '千语吖'), (3414, '3人行'), (3415, '大狗贼'), (3416, '叶音符'), (3417, '大吊队'), (3418, '哥哥好'), (3419, '傲娇豆'), (3420, '柒月一'), (3421, '蓝票'), (3422, '卡师傅'), (3423, '入侵怪'), (3424, '夏优'), (3425, '九日'), (3426, '骚飞'), (3427, '预言凯'), (3428, '洛克K'), (3429, '林蒙'), (3430, '一万五'), (3431, '莫塔'), (3432, '中憬'), (3433, '鶸'), (3434, '寒一夜'), (3435, '真傲娇'), (3436, '想弟弟'), (3437, '老铁团'), (3438, '大饼干'), (3439, '乖女王'), (3440, '渣渣Q'), (3441, 'Amaz'), (3442, '小柚几'), (3443, '小渣男'), (3444, '污师团'), (3445, '一玥'), (3446, '铅笔盒'), (3447, 'A小妖'), (3448, '渣渣猎'), (3449, '王小瘙'), (3450, '印红'), (3451, '段灬友'), (3452, '雷疯'), (3453, '口嗨'), (3454, '浅丶陌'), (3455, '灵儿'), (3456, '岚之山'), (3457, 'LGD'), (3458, '融Zz'), (3459, '杀手S'), (3460, 'C小哈'), (3461, '遇白'), (3462, '7293'), (3463, '蛙酱'), (3464, '麒麟团'), (3465, '宋人头'), (3466, '大耀呦'), (3467, '游弋'), (3468, '海草酱'), (3469, '小聋瞎'), (3470, '鹌鹑'), (3471, '溜溜哒'), (3472, '加夕夕'), (3473, '王慕霸'), (3474, '老猫丶'), (3475, '猛猛'), (3476, '肉粉丝'), (3477, '蹦蹦呀'), (3478, '冷鸽'), (3479, '萌小雨'), (3480, '夏末M'), (3481, '涛哥弟'), (3482, '魅力'), (3483, '龙腾'), (3484, '书笙'), (3485, '虾米哟'), (3486, '丶十一'), (3487, '鱼桑'), (3488, '250'), (3489, '至尊俊'), (3490, '甄爱粉'), (3491, '薄荷新'), (3492, '放弃o'), (3493, '鸡汤'), (3494, 'z小二'), (3495, '痴汉丶'), (3496, '叹世尘'), (3497, '風月'), (3498, '木子系'), (3499, '花Hz'), (3500, '曦梦i'), (3501, '520U'), (3502, '胖胖爪'), (3503, '小小飘'), (3504, '潮汕杰'), (3505, '青词'), (3506, '抠子'), (3507, '婕妤'), (3508, '小软m'), (3509, '降温'), (3510, '冰妞'), (3511, '長久'), (3512, '君子也'), (3513, '炮酱i'), (3514, '骚队'), (3515, '阿布i'), (3516, '耀西'), (3517, '喵玩具'), (3518, '林小姐'), (3519, '大海i'), (3520, '西格杏'), (3521, '丷晴天'), (3522, '林Q'), (3523, '吾念'), (3524, '灰灰酱'), (3525, '可樂宝'), (3526, '久哥哥'), (3527, '339'), (3528, '恶魔'), (3529, '七个我'), (3530, '九剑丶'), (3531, '9好运'), (3532, '歌神清'), (3533, '萌啾啾'), (3534, '凯瑞尔'), (3535, '9438'), (3536, '格调M'), (3537, '绝S世'), (3538, '麒刘海'), (3539, '样宝宝'), (3540, '花村'), (3541, '好哥们'), (3542, '小徐子'), (3543, '遇见x'), (3544, '彦三岁'), (3545, 'TwoT'), (3546, '静静酱'), (3547, '鹿总总'), (3548, '神貂'), (3549, '小糊歌'), (3550, '丁小高'), (3551, '油条'), (3552, '豪门卫'), (3553, '游乐乐'), (3554, 'XQ林'), (3555, '破盆'), (3556, '盔盔王'), (3557, '丶沐木'), (3558, '小女污'), (3559, '乌鸦'), (3560, '赵番茄'), (3561, '蔡猜猜'), (3562, '卢本伟'), (3563, '雪娃娃'), (3564, '瞎比帅'), (3565, '阿冷灬'), (3566, '老戴'), (3567, '别打乐'), (3568, '洋仔Q'), (3569, '赵猥琐'), (3570, '秋风'), (3571, '槑老师'), (3572, '木工'), (3573, '口苗'), (3574, '丁酱'), (3575, '战神志'), (3576, '帅比风'), (3577, 'RUG'), (3578, '呆萌萝'), (3579, '徐丶氏'), (3580, 'TDs'), (3581, '土豆芽'), (3582, '赛文柒'), (3583, '凜87'), (3584, '小乌贼'), (3585, '阿狸'), (3586, '阿凯K'), (3587, '喵晚安'), (3588, '小逗包'), (3589, '小闷骚'), (3590, '泪丶落'), (3591, '炜老板'), (3592, '火乐'), (3593, '独秀迹'), (3594, '老铁会'), (3595, '好家伙'), (3596, '乱雨'), (3597, '绝尘懵'), (3598, '3号'), (3599, '131'), (3600, 'Eva'), (3601, '大冷'), (3602, '可友哆'), (3603, '帅比乌'), (3604, '饭煲7'), (3605, '满仓红'), (3606, '骚无情'), (3607, 'tumi'), (3608, '萌瘤瘤'), (3609, '法兰蒂'), (3610, '罗细基'), (3611, '不网戀'), (3612, '山人丶'), (3613, '七爷'), (3614, '骚皮6'), (3615, '正义天'), (3616, '蒙蒙m'), (3617, '哑YM'), (3618, '按摩师'), (3619, '失忆忆'), (3620, 'pp猪'), (3621, '腿鸽鸽'), (3622, '刮神'), (3623, '墨烟'), (3624, '丁叮阿'), (3625, '娜哥哥'), (3626, '300斤'), (3627, '铆钉鱼'), (3628, '翔凯吖'), (3629, '913'), (3630, '小二林'), (3631, '十oV3'), (3632, '猫之神'), (3633, '独秀1'), (3634, '魔神宝'), (3635, 'l魔君'), (3636, '小蛙蛙'), (3637, '猛汉丶'), (3638, '白溟'), (3639, '太大了'), (3640, '我邪恶'), (3641, '黑瞎子'), (3642, '又神'), (3643, '基米'), (3644, '高畗帅'), (3645, '吃小菜'), (3646, '南轲'), (3647, '流沙o'), (3648, '安若蓝'), (3649, '许仙'), (3650, '葱芯绿'), (3651, '漆家军'), (3652, '玖99'), (3653, '又沫'), (3654, '猛男'), (3655, '吃肉包'), (3656, '爱跳兔'), (3657, '瓜皮范'), (3658, '熙真呀'), (3659, '启文'), (3660, '明凶秀'), (3661, '一一啦'), (3662, 'JSA'), (3663, '李霣龙'), (3664, '酒神'), (3665, 'WDK'), (3666, '野猪啊'), (3667, '礼物a'), (3668, '深情乔'), (3669, '大帅Q'), (3670, '阳神c'), (3671, '小眫子'), (3672, '独苗刀'), (3673, '小帅丶'), (3674, '逗神茄'), (3675, '墨god'), (3676, '梦老贼'), (3677, '南二狗'), (3678, '向日菊'), (3679, '皮皮淡'), (3680, '苏蓝'), (3681, '斯祥丶'), (3682, '皮神程'), (3683, '爱次鱼'), (3684, '围静呀'), (3685, '死神秀'), (3686, '443'), (3687, '信陵'), (3688, '老生煎'), (3689, '委屈屈'), (3690, '北萌'), (3691, '奈奈丶'), (3692, '小赢僧'), (3693, '埋埋'), (3694, '成帅V'), (3695, '九久'), (3696, '菟菟酱'), (3697, '老丶高'), (3698, '科美'), (3699, '茉蓝丶'), (3700, '朱仙'), (3701, '仙班'), (3702, '6神丿'), (3703, '鴻天赐'), (3704, '纯纯仔'), (3705, '锦小年'), (3706, 'AC'), (3707, '小光子'), (3708, '不醒喵'), (3709, '未寻'), (3710, '苟鸡沐'), (3711, '闹君'), (3712, '菇艿艿'), (3713, '暴民'), (3714, '264'), (3715, '日月8'), (3716, '冷三岁'), (3717, '绿旋春'), (3718, '旺半仙'), (3719, '仙灵龙'), (3720, '小尛帅'), (3721, '可可悦'), (3722, '对7'), (3723, '李白条'), (3724, '护酥堡'), (3725, '教乀父'), (3726, '有痕'), (3727, '玉女鲸'), (3728, 'GT'), (3729, '婉清'), (3730, '浩博呦'), (3731, '福28'), (3732, '鬼豪'), (3733, '南斗'), (3734, '我萱妳'), (3735, '火星包'), (3736, '小立人'), (3737, '奥西瓜'), (3738, '酸奶盒'), (3739, '王大皮'), (3740, '罗汉团'), (3741, 'WWAN'), (3742, '小豆浆'), (3743, '周双虎'), (3744, '你蓝神'), (3745, '美6'), (3746, '爷没钱'), (3747, '唐甜甜'), (3748, '鲸囤'), (3749, '钟儿美'), (3750, '誓约'), (3751, '战神'), (3752, '乐秃秃'), (3753, 'zx呀'), (3754, '可爱粹'), (3755, '君妹o'), (3756, '大绅士'), (3757, '叶灵'), (3758, '迷鹿s'), (3759, '戒网'), (3760, 'Eddd'), (3761, '水煮肉'), (3762, '花太香'), (3763, '奶咖咖'), (3764, '瓜皮晚'), (3765, '神坑哀'), (3766, '溫丶柔'), (3767, '童芙酥'), (3768, '骚易丶'), (3769, '哈47'), (3770, 'Mi鹿'), (3771, '黑灬蛋'), (3772, '雨娜娜'), (3773, '小裆家'), (3774, '果汁儿'), (3775, '咸鱼酒'), (3776, '蛇蛇蛇'), (3777, '萬劍一'), (3778, '唐逗'), (3779, '粒'), (3780, '胖胖C'), (3781, '小阿锟'), (3782, '念白'), (3783, '传奇迷'), (3784, '躺夏'), (3785, 'G513'), (3786, '丶染指'), (3787, 'MEIY'), (3788, '猴仔'), (3789, '茶茶啊'), (3790, '老鬼'), (3791, '星河家'), (3792, '归洛浦'), (3793, '浪六'), (3794, '鸽王'), (3795, '崇书生'), (3796, '珍滴皮'), (3797, '凡森'), (3798, '秦史皇'), (3799, '小8路'), (3800, '小鹹魚'), (3801, '小小狮'), (3802, '方晨式'), (3803, '小猪崽'), (3804, '拜瑞'), (3805, '废铁叔'), (3806, '推推棒'), (3807, 'Azi'), (3808, '火乍'), (3809, '净空灵'), (3810, '皮皮拉'), (3811, '小迷狐'), (3812, '丁皇'), (3813, '明丿月'), (3814, '小酷K'), (3815, '漫步呀'), (3816, '爱猫'), (3817, '潇洒洒'), (3818, '鳕鱼'), (3819, '小福元'), (3820, '叶灬子'), (3821, '胡彦祖'), (3822, '伏地摩'), (3823, '总嘟府'), (3824, '星漾X'), (3825, '炸翻天'), (3826, '么茉哒'), (3827, '麻辣涛'), (3828, '干豆腐'), (3829, '张大湿'), (3830, 'G木兰'), (3831, '右右'), (3832, '昆仔'), (3833, '兔爷儿'), (3834, '仙女怡'), (3835, '卡卡喔'), (3836, '叶子萌'), (3837, '过儿丨'), (3838, 'A大M'), (3839, '卡好多'), (3840, '比安卡'), (3841, '晗晗哟'), (3842, '可爱嗨'), (3843, '宁采臣'), (3844, '我冰'), (3845, '浪鸟'), (3846, '元首巴'), (3847, '玫有钱'), (3848, '真寂寞'), (3849, '紫宸'), (3850, '帅伪装'), (3851, '泥巴豪'), (3852, '烽火令'), (3853, '褶可爱'), (3854, '九黎灬'), (3855, '沙漏哥'), (3856, '胖玥玥'), (3857, '阿聪'), (3858, '宇啾'), (3859, 'N浩哥'), (3860, '苏橙'), (3861, '奶'), (3862, '蠢萌叔'), (3863, '叶漂亮'), (3864, '2晴'), (3865, '姚之家'), (3866, '十四'), (3867, '兜风'), (3868, '盒贩'), (3869, '转圈圈'), (3870, '软略略'), (3871, '瓜皮跳'), (3872, '欧洲翅'), (3873, '三黄喵'), (3874, '无惜惜'), (3875, '逆风宇'), (3876, '猪猪磊'), (3877, '笑傲君'), (3878, 'AJ'), (3879, '南小瑾'), (3880, '哭红'), (3881, '森林丶'), (3882, '鯊呼呼'), (3883, '阿涛粉'), (3884, 'S鱼鹰'), (3885, '生辰刚'), (3886, '林正英'), (3887, '鹿好听'), (3888, '汪星星'), (3889, '菲宝宝'), (3890, '大大帮'), (3891, '惜雪'), (3892, '宝聚缘'), (3893, '三千萬'), (3894, '霖萌'), (3895, '小天仇'), (3896, '赵小薇'), (3897, '周馨馨'), (3898, '17U'), (3899, '大白吐'), (3900, '大锤丶'), (3901, '夸父吧'), (3902, '天T'), (3903, '咸余'), (3904, '猪猪7'), (3905, '庄炸庙'), (3906, '吹牛鸟'), (3907, '凉茶k'), (3908, '好师弟'), (3909, '六元宝'), (3910, '优优球'), (3911, '浮神'), (3912, '小路霸'), (3913, '荔荔枝'), (3914, '月半西'), (3915, '壳壳壳'), (3916, '三神丶'), (3917, '希噢'), (3918, '肖白七'), (3919, '逍遥'), (3920, '诸葛槑'), (3921, '鸣圣'), (3922, '舟润发'), (3923, '211'), (3924, '喵二娘'), (3925, 'xyao'), (3926, '諸葛瑾'), (3927, '追星族'), (3928, '蜘小蛛'), (3929, '研二'), (3930, '柒梦阁'), (3931, '西决啊'), (3932, '夕宝R'), (3933, '朴妹'), (3934, '伊筒'), (3935, '婉爷的'), (3936, '大猫牌'), (3937, '央家军'), (3938, '秀梦灬'), (3939, '鬼故事'), (3940, '蒲美美'), (3941, '屠龍刀'), (3942, '栗子说'), (3943, 'A阿杰'), (3944, '黄雀'), (3945, '汏汏军'), (3946, '小孤野'), (3947, '萧弘'), (3948, '80it'), (3949, '奶九'), (3950, '4154')]),
        ),
    ]
