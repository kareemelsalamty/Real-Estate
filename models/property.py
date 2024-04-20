from odoo import models, fields, api
from odoo.exceptions import ValidationError

class property(models.Model):

    _name = 'property'

    name = fields.Char(required=True)
    description = fields.Text()
    post_code = fields.Char(required=True)
    data_availability = fields.Date()
    expected_price = fields.Float(digits=(0,6))
    selling_price = fields.Float()
    diff = fields.Float(compute='_compute_diff')
    bedrooms = fields.Integer(required=True)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West')
    ])
    owner_id=fields.Many2one('owner')
    tag_ids=fields.Many2many('tag')
    state =fields.Selection ([
        ('draft','Draft') ,
        ('pending', 'Pending') ,
        ('sold', 'Sold'),
    ],default ='draft')


    _sql_constraints = [
        ('unique_name', 'unique(name)', 'this name is exist !')
    ]
    @api.depends('expected_price','selling_price')
    def _compute_diff (self):
        for rec in self:
            rec.diff =rec.expected_price - rec.selling_price

    @api.onchange('expected_price')
    def _onchange_expected_price(self):
        for rec in self:
            print("inside onchange method")
            return {
                'warning':{'title':'warning','message':'neagative value','type':'notification'}
            }

    @api.constrains('bedrooms')
    def _check_bedrooms_greater_zero(self):
        for rec in self:
            if rec.bedrooms == 0:
                raise ValidationError("please add valid number of bedrooms!")

    def action_draft(self):
        for rec in self:
            print("inside draft action ")
            rec.state = 'draft'
        # or
        # rec.write ({
             # 'state' : 'draft'
        # })

    def action_pending(self):
        for rec in self:
            print("inside pending action ")
            rec.state = 'pending'

    def action_sold(self):
        for rec in self:
            print("inside sold action ")
            rec.state = 'sold'


    @api.model_create_multi
    def create(self, vals):
        res = super(property, self).create(vals)
        print("inside create method ")
        #logic
        return res

    @api.model
    def _search(self, domain, offset=0, limit=None, order=None, access_right_uid=None, count=False):
        res = super(property, self)._search(domain, offset=offset, limit=limit, order=order)
        print("inside search method ")
        # logic
        return res

    def write(self, vals):
        res = super(property, self).write(vals)
        print("inside write method ")
        # logic
        return res

    def unlink(self):
        res = super(property, self).unlink()
        print("inside unlink method ")
        # logic
        return res


