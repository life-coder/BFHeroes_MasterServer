(function(b) {
	var d = b.jQuery,
		c = b._,
		e = b.Backbone,
		a = b.BFH;
	d(function() {
		var h = '<span class="icon_shadow" /><span class="icon_skin"></span><span class="icon_facialHair"></span><span class="icon_hair"></span><span class="facialFeatures"></span>';

		function j(l) {
			d(l)
				.removeClass("disabled")
				.data("disabled", false)
		}

		function f(l) {
			d(l)
				.addClass("disabled")
				.data("disabled", true)
		}
		if (a && a.barbershopSettings) {
			var g = e.Model.extend({
					defaults: function() {
						return {
							hairView: "baseMSGAppearanceHairStyleStats"
						}
					}
				}),
				k = e.View.extend({
					el: "#createHero",
					template: c.template(d("#hero-template")
						.html() + " "),
					events: {
						"click .faction li, .heroClass li, .hair li, .facialHair li, .skinColor li, .hairColor li": "changeAttribute",
						"click #saveHero": "save",
						"click #randomHero": "randomize",
						"click .hairSelector h2": "changeHairTab",
						"mouseover .faction li, .heroClass li": "changeHelp",
						"mouseout .faction li, .heroClass li": "defaultHelp",
						"click .nameSelector #cancelName": "cancelName",
						"click .nameSelector #chooseName": "chooseName"
					},
					initialize: function() {
						var l = this;
						this.facialHairOptions = {
							1: [],
							2: []
						};
						this.hairOptions = {
							1: [],
							2: []
						};
						this.hairColorOptions = [];
						this.skinColorOptions = [];
						this.factionOptions = [];
						this.heroClassOptions = [];
						this.model.set("facial_ui_name", parseInt(this.$("#facial_ui_name")
							.val(), 10));
						this.model.set("baseMSGFactionStats", parseInt(this.$("#baseMSGFactionStats")
							.val(), 10));
						this.model.set("baseMSGPersonaClassStats", parseInt(this.$("#baseMSGPersonaClassStats")
							.val(), 10));
						this.model.set("baseMSGAppearanceHairStyleStats", parseInt(this.$("#baseMSGAppearanceHairStyleStats")
							.val(), 10));
						this.model.set("baseMSGAppearanceSkinToneStats", parseInt(this.$("#baseMSGAppearanceSkinToneStats")
							.val(), 10));
						this.model.set("haircolor_ui_name", parseInt(this.$("#haircolor_ui_name")
							.val(), 10));
						this.oldValues = a.barbershopSettings.barbershop && this.model.toJSON();
						this.model.bind("change", this.render, this);
						if (a.accountData) {
							a.accountData.bind("change", this.render, this)
						}
						this.$("#facial_ui_name option")
							.each(function() {
								var n = parseInt(d(this)
										.val(), 10),
									m = parseInt(d(this)
										.parent("optgroup")
										.attr("label"), 10);
								l.facialHairOptions[m].push(n);
								d("<li />")
									.data("id", n)
									.addClass("facialHair" + n)
									.html(h)
									.appendTo("#createHero .characteristics .facialHair .faction" + m)
							});
						this.$("#baseMSGAppearanceHairStyleStats option")
							.each(function() {
								var n = parseInt(d(this)
										.val(), 10),
									m = parseInt(d(this)
										.parent("optgroup")
										.attr("label"), 10);
								l.hairOptions[m].push(n);
								d("<li />")
									.data("id", n)
									.addClass("hair" + n)
									.html(h)
									.appendTo("#createHero .characteristics .hair .faction" + m)
							});
						this.$("#baseMSGAppearanceSkinToneStats option")
							.each(function() {
								var m = parseInt(d(this)
									.val(), 10);
								l.skinColorOptions.push(m);
								d("<li />")
									.data("id", m)
									.addClass("skinColor" + m)
									.html(h)
									.prependTo("#createHero .characteristics .skinColor")
							});
						c.each([1, 3, 5, 2, 4], function(m) {
							l.hairColorOptions.push(m);
							d("<li />")
								.data("id", m)
								.addClass("hairColor" + m)
								.appendTo("#createHero .characteristics .hairColor")
						});
						this.$("#baseMSGPersonaClassStats option")
							.each(function() {
								var m = parseInt(d(this)
									.val(), 10);
								l.heroClassOptions.push(m);
								d("<li />")
									.data("id", m)
									.addClass("heroClass" + m)
									.appendTo("#createHero .heroType .heroClass")
							});
						this.$("#baseMSGFactionStats option")
							.each(function() {
								var m = parseInt(d(this)
									.val(), 10);
								l.factionOptions.push(m);
								d("<li />")
									.data("id", m)
									.addClass("faction" + m)
									.appendTo("#createHero .heroType .faction")
							});
						this.defaultHelp();
						c.bindAll(this, "changeAttribute")
					},
					render: function() {
						this.$el.removeClass()
							.addClass("selectedFaction" + this.model.get("baseMSGFactionStats"))
							.addClass("selectedHeroClass" + this.model.get("baseMSGPersonaClassStats"))
							.addClass("selectedHair" + this.model.get("baseMSGAppearanceHairStyleStats"))
							.addClass("selectedFacialHair" + this.model.get("facial_ui_name"))
							.addClass("selectedHairColor" + this.model.get("haircolor_ui_name"))
							.addClass("selectedSkinColor" + this.model.get("baseMSGAppearanceSkinToneStats"));
						if (a.barbershopSettings.barbershop) {
							this.$el.addClass("barbershop");
							if (a.accountData.get("_PF") >= parseInt(a.barbershopSettings.price, 10)) {
								this.$(".fund")
									.hide();
								if (c.isEqual(this.oldValues, this.model.toJSON())) {
									f(this.$("#saveHero")
										.show())
								} else {
									j(this.$("#saveHero")
										.show())
								}
							} else {
								this.$("#saveHero")
									.hide();
								this.$(".fund")
									.show()
							}
						}
					},
					remove: function() {
						e.View.prototype.remove.call(this)
					},
					changeAttribute: function(q) {
						var o = (function() {
								var s = d(q.currentTarget);
								if (s.data("id")) {
									s = s.closest("li")
								}
								return s
							}()),
							n = o.closest("ul"),
							l = n.data("type"),
							p = o.data("id"),
							m, r;
						if (this.model.get(l) !== p) {
							this.model.set(l, p);
							this.$("#" + l)
								.val(p);
							if (l === "baseMSGFactionStats") {
								m = c.indexOf(this.hairOptions[p === 1 ? 2 : 1], this.model.get("baseMSGAppearanceHairStyleStats"), true);
								r = c.indexOf(this.facialHairOptions[p === 1 ? 2 : 1], this.model.get("facial_ui_name"), true);
								this.model.set("baseMSGAppearanceHairStyleStats", this.hairOptions[p][m]);
								this.$("#baseMSGAppearanceHairStyleStats")
									.val(this.hairOptions[p][m]);
								this.model.set("facial_ui_name", this.facialHairOptions[p][r]);
								this.$("#facial_ui_name")
									.val(this.facialHairOptions[p][r])
							}
							if (l === "baseMSGFactionStats" || l === "baseMSGPersonaClassStats") {
								this.defaultHelp()
							}
						}
					},
					changeHelp: function(p) {
						var m = d(p.target)
							.closest("ul")
							.data("type"),
							o = d(p.target)
							.data("id"),
							l = a.barbershopSettings.help[m][o][0],
							n = a.barbershopSettings.help[m][o][1];
						this.updateHelp(l, n)
					},
					updateHelp: function(m, l) {
						this.$(".help .header")
							.html(m);
						this.$(".help .bodyText")
							.html(l)
					},
					defaultHelp: function() {
						var l = a.barbershopSettings.help["default"][0],
							m = a.barbershopSettings.help["default"][1].replace("%faction%", a.barbershopSettings.help.baseMSGFactionStats[this.model.get("baseMSGFactionStats")][0])
							.replace("%heroClass%", a.barbershopSettings.help.baseMSGPersonaClassStats[this.model.get("baseMSGPersonaClassStats")][0]);
						this.updateHelp(l, m)
					},
					chooseName: function(m) {
						if (d(m.target)
							.data("disabled")) {
							return
						}
						f(d("#chooseName"));
						f(d("#cancelName"));
						var l = this.$(".nameSelector input")
							.val();
						this.$("#nameCharacterText")
							.val(l);
						this.$(".nameSelector")
							.siblings(".error")
							.hide();
						d.ajax({
								type: "post",
								url: a.barbershopSettings.name_url,
								data: {
									heroName: l
								},
								dataType: "json"
							})
							.success(function() {
								d(".nameSelector input")
									.after(d('<span class="heroName"/>')
										.text(l))
									.remove();
								d("#createHero")
									.submit()
							})
							.error(function() {
								j(d("#chooseName"));
								j(d("#cancelName"));
								d(".nameSelector")
									.siblings(".error")
									.show()
							})
					},
					cancelName: function() {
						this.$(".nameSelector")
							.parent(".overlay")
							.fadeOut();
						this.$(".nameSelector")
							.siblings(".error")
							.hide();
						this.$(".help")
							.show();
						j(d("#saveHero"))
					},
					save: function(l) {
						if (d(l.target)
							.data("disabled")) {
							return
						}
						f(l.target);
						if (!c.isEqual(this.oldValues, this.model.toJSON())) {
							d("#createHero")
							var heroname = prompt("Please enter your new hero name:", "Enter Name Here")
							if (heroname == null || heroname == "") {
								document.getElementById("loginError")
									.style.display = "block";
								document.getElementById("error")
									.innerHTML = "<p>Whoops! You didn't anwser question about hero name!<\/p>";
								document.getElementById("loginForm")
									.className = "loginForm"
							} else {
								document.getElementById("nameCharacterText")
									.value = heroname
								document.getElementById("createHero")
									.submit()
							}

						}
					},
					randomize: function() {
						var l = {
							baseMSGFactionStats: this.factionOptions[Math.floor(Math.random() * this.factionOptions.length)],
							baseMSGPersonaClassStats: this.heroClassOptions[Math.floor(Math.random() * this.heroClassOptions.length)],
							haircolor_ui_name: this.hairColorOptions[Math.floor(Math.random() * this.hairColorOptions.length)],
							baseMSGAppearanceSkinToneStats: this.skinColorOptions[Math.floor(Math.random() * this.skinColorOptions.length)]
						};
						l.baseMSGAppearanceHairStyleStats = this.hairOptions[l.baseMSGFactionStats][Math.floor(Math.random() * this.hairOptions[l.baseMSGFactionStats].length)];
						l.facial_ui_name = this.facialHairOptions[l.baseMSGFactionStats][Math.floor(Math.random() * this.facialHairOptions[l.baseMSGFactionStats].length)];
						this.model.set(l);
						this.$("#baseMSGFactionStats")
							.val(this.model.get("baseMSGFactionStats"));
						this.$("#baseMSGPersonaClassStats")
							.val(this.model.get("baseMSGPersonaClassStats"));
						this.$("#haircolor_ui_name")
							.val(this.model.get("haircolor_ui_name"));
						this.$("#baseMSGAppearanceHairStyleStats")
							.val(this.model.get("baseMSGAppearanceHairStyleStats"));
						this.$("#baseMSGAppearanceSkinToneStats")
							.val(this.model.get("baseMSGAppearanceSkinToneStats"));
						this.$("#facial_ui_name")
							.val(this.model.get("facial_ui_name"));
						this.defaultHelp()
					},
					changeHairTab: function(l) {
						this.$(".hairSelector")
							.removeClass("baseMSGAppearanceHairStyleStats facial_ui_name")
							.addClass(d(l.target)
								.data("tab"))
					}
				});
			var i = new k({
				model: new g()
			});
			i.render()
		}
	})
}(this));