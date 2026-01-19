from odoo import models, fields, api

class Digizilla(models.Model):
    _name = 'digizilla.digizilla'
    _description = 'Digizilla'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True, tracking=True)
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female')],
        tracking=True
    )
    country_id = fields.Many2one('res.country', string='Country')
    birth_date = fields.Date(string='Birth Date')
    age = fields.Integer(string='Age', compute='_compute_age')
    tag_ids = fields.Many2many('res.partner.category', string='Tags')
    customer_id = fields.Many2one(
        'res.partner',
        string='Customer',
        required=True,
        tracking=True
    )
    no_of_sales_orders = fields.Integer(
        string='No. of Sales Orders',
        compute='_compute_sales_orders'
    )
    notes = fields.Html(string='Notes')
    comments = fields.Char(string='Comments')

    @api.depends('birth_date')
    def _compute_age(self):
        today = fields.Date.today()
        for rec in self:
            rec.age = 0
            if rec.birth_date:
                rec.age = (today - rec.birth_date).days // 365

    @api.depends('customer_id')
    def _compute_sales_orders(self):
        for rec in self:
            rec.no_of_sales_orders = 0
            if rec.customer_id:
                rec.no_of_sales_orders = self.env['sale.order'].search_count([
                    ('partner_id', '=', rec.customer_id.id)
                ])
