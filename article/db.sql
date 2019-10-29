CREATE TABLE `article` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `title` varchar(255) DEFAULT NULL COMMENT '文章标题',
  `summary` varchar(255) DEFAULT NULL COMMENT '文章来源',
  `publish_time` datetime DEFAULT NULL COMMENT '文章发布时间',
  `html` longtext COMMENT '文章内容',
  `url` varchar(255) DEFAULT NULL COMMENT '文章地址',
  `site_name` varchar(255) DEFAULT NULL COMMENT '站点名称',
  `site_module` varchar(255) DEFAULT NULL COMMENT '站点模块',
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `batch_id` varchar(255) DEFAULT NULL COMMENT '批次号',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;